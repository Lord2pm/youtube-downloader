function activeFormat(index) {
	let formats = document.getElementsByClassName("formato");
	let formatHidden = document.getElementsByClassName("formato-hidden");

	for (let i = 0; i < formats.length; i++) {
		if (index - 1 == i) {
			console.log(formats);
			formats[i].classList.add("active");
			formatHidden.innerText = formats[i].innerText;
			formatHidden.value = formats[i].innerText;
			formatHidden.innerText = "Ola";
		} else {
			formats[i].classList.remove("active");
		}
	}
}

let closeButton = document.querySelector(".close-msg");
let msg = document.querySelector(".mensagens");

setTimeout(() => {
	msg.style.display = "none";
}, 5000);

closeButton.addEventListener("click", () => {
	msg.style.display = "none";
});
