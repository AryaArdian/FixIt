from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from services.catalog import CATEGORIES, SERVICES, get_category, get_service, list_services
from services.diagnosis import diagnose as run_diagnosis

main = Blueprint("main", __name__)
ALLOWED = {"png", "jpg", "jpeg", "webp"}


@main.route("/")
def index():
    top = sorted(SERVICES, key=lambda s: -s["rating"])[:3]
    return render_template("index.html", categories=CATEGORIES, services=top)


@main.route("/diagnose")
@main.route("/diagnose/<slug>", methods=["GET", "POST"])
def diagnose_page(slug=None):
    cat = get_category(slug) if slug else None
    if slug and not cat:
        abort(404)
    if request.method == "POST":
        desc = request.form.get("description", "").strip()
        extra = request.form.get("extra", "").strip()
        photo = request.files.get("photo")
        error = None
        if len(desc) < 10:
            error = "Describe the problem in at least 10 characters."
        elif photo and photo.filename and photo.filename.rsplit(".", 1)[-1].lower() not in ALLOWED:
            error = "Photo must be a PNG, JPG, or WEBP file."
        if error:
            flash(error, "error")
            return render_template("diagnose.html", categories=CATEGORIES, cat=cat, form=request.form), 400
        # No storage: the problem text travels in the URL, so the result can be refreshed or shared.
        flash("Diagnosis ready.", "success")
        return redirect(url_for("main.result", slug=cat["slug"], q=f"{desc} {extra}".strip()[:500]))
    return render_template("diagnose.html", categories=CATEGORIES, cat=cat, form=None)


@main.route("/result/<slug>")
def result(slug):
    cat = get_category(slug)
    if not cat:
        abort(404)
    text = request.args.get("q", "").strip()
    if not text:
        return redirect(url_for("main.diagnose_page", slug=slug))
    r = {"icon": cat["icon"], "cat_name": cat["name"], "description": text}
    return render_template("result.html", r=r, d=run_diagnosis(slug, text))


@main.route("/services")
def services():
    active = request.args.get("category", "")
    return render_template("services.html", services=list_services(active), categories=CATEGORIES, active=active)


@main.route("/services/<int:service_id>")
def service_detail(service_id):
    s = get_service(service_id)
    if not s:
        abort(404)
    return render_template("service_detail.html", s=s)
