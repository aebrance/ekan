anime({
    targets: '#ekan_logo g path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 2500,
    delay: function (el, i) { return i * 350 },
    direction: 'alternate',
    loop: false,
});