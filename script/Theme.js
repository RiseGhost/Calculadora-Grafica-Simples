const Theme_button = document.getElementById("Theme")
const Body = document.getElementById("body")
const Input_number = document.getElementById("input_number")
const TittleBar = document.getElementById("tittlebar")
const Canvas = document.getElementById("canvas")
const Result_Label = document.getElementById("result")
const Step = document.getElementById("step")

function pause_all_animation(){
    Body.style.animationPlayState = "paused"
    Input_number.style.animationPlayState = "paused"
    TittleBar.style.animationPlayState = "paused"
    Canvas.style.animationPlayState = "paused"
    Theme_button.style.animationPlayState = "paused"
}

function running_all_animation(){
    Body.style.animationPlayState = "running"
    Input_number.style.animationPlayState = "running"
    TittleBar.style.animationPlayState = "running"
    Canvas.style.animationPlayState = "running"
    Theme_button.style.animationPlayState = "running"
}

Theme_button.addEventListener("click", () => {
    const Theme_icon = document.getElementById("Theme_icon").innerText
    if (Theme_icon == "dark_mode"){
        pause_all_animation()
        document.getElementById("Theme_icon").innerText = "light_mode"
        Body.style.animation = "lightmode 4s"
        Input_number.style.animation = "ligthmode_input 4s"
        Theme_button.style.animation = "ligthmode_input 4s"
        TittleBar.style.animation = "ligthmode_tittlebar 4s"
        Canvas.style.animation = "lightmode_canvas 4s"
        setTimeout( function () {
            Body.style.backgroundColor = "#95b6ac"
            Input_number.style.backgroundColor = "#ebf2f2"
            Input_number.style.color = "#787878"
            Theme_button.style.backgroundColor = "#ebf2f2"
            Theme_button.style.color = "#787878"
            Result_Label.color = "#787878"
            TittleBar.style.backgroundColor = "rgba(130,130,130,1)"
            Canvas.style.backgroundColor = "#ade0db"
            Step.style.backgroundColor = "#7caca7"
        }, 3990)
        running_all_animation()
    }   else{
        document.getElementById("Theme_icon").innerText = "dark_mode"
        pause_all_animation()
        Body.style.animation = "darkmode 4s"
        Input_number.style.animation = "darkmode_input 4s"
        Theme_button.style.animation = "darkmode_input 4s"
        TittleBar.style.animation = "darkmode_tittlebar 4s"
        Canvas.style.animation = "darkmode_canvas 4s"
        setTimeout( function () {
            Body.style.backgroundColor = "#012b3e"
            Input_number.style.backgroundColor = "#00988d"
            Input_number.style.color = "#fef5c8"
            Theme_button.style.backgroundColor = "#00988d"
            Theme_button.style.color = "#fef5c8"
            Result_Label.style.color = "#fef5c8"
            TittleBar.style.backgroundColor = "rgba(0,0,0,1)"
            Canvas.style.backgroundColor = "#2c6b74"
            Step.style.backgroundColor = "#02496a"
        }, 3990)
        running_all_animation()
    }
    console.log(Theme_icon)
})