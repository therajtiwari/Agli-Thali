function recipe(name) {
  window.location.href = Flask.url_for("recipe", { name: name });
}
