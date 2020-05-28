const checkBtn = document.querySelector(".checkBtn")

function handleClick() {
    if (checkBtn.innerHTML === "⭕") {
        checkBtn.innerHTML = "❌"
    } else {
        checkBtn.innerHTML = "⭕"
    }
}
function init() {
    checkBtn.addEventListener("click", handleClick)
}

init()
