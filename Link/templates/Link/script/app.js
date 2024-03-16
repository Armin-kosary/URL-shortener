document.querySelector(".copy-svg").addEventListener("click", function () {
    let inputUrl = document.querySelector("#url-shortened");
    let notification = document.querySelector(".notification");

    inputUrl.select();
    document.execCommand("copy");
    notification.style.display = "inline";
    setInterval(function () {
        notification.style.display = "none";
    }, 2000);
});