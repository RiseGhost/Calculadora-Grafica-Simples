const result = document.getElementById("result")
const painel = document.getElementById("step")

result.addEventListener("mouseover", () => {
    document.getElementById("step").style.display = "flex"
    console.log("Hello")
})

painel.addEventListener("mouseleave", () => {
    document.getElementById("step").style.display = "none"
})