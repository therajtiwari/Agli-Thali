function recipe(name) {
  window.location.href = Flask.url_for("recipe", { name: name });
}
$(".owl-carousel").owlCarousel({
  loop: true,
  nav: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    720: {
      items: 2,
    },
    960: {
      items: 3,
    },
    1140: {
      items: 4,
    },
    1500: {
      items: 5,
    },
  },
});
