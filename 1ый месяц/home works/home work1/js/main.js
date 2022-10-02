
console.log("hello world");

let input = document.getElementsByClassName("photo_sender");
input[0].addEventListener("click" ,() => {
    alert("Все отправлено");

    alert("Шучу. Куда мне их отправлять? )))");
});


let photos = document.getElementsByClassName("photo");

for( let i = 0; i < photos.length; i++) {
    photos[i].addEventListener("click", () => {
        photos[i]
    })
}
