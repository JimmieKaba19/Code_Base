const container = document.querySelector(".container");
let containerSize = document.querySelector(".container").offsetWidth;
const setGrid = document.querySelector(".grid-btn");
const presentGrid = document.querySelector(".present-btn");
let isDrawing = false;

function randomColor() {
    let color = [];
    for(let i = 0; i < 3; i++){
        color.push(Math.floor(Math.random() * 256));
    }
    return `rgb(${color.join(",")})`
}

function makeGrid(boxesPerFace){
    container.innerHTML = "";
    const totalGridItems = boxesPerFace ** 2;
    for (let i = 0; i < totalGridItems; i++) {
        const gridItem = document.createElement("div");
        gridItem.classList.add("grid-item");
        container.appendChild(gridItem);
    }
    container.style.width = `${boxesPerFace * (containerSize / 16)}px`;
    container.style.height = `${boxesPerFace * (containerSize / 16)}px`;

    presentGrid.addEventListener("click", () => {
        alert(`Current total: ${boxesPerFace}`);
    });
}

function gridSet(){
    let boxesPerFace = prompt("Enter number of boxes per grid side (boxes < 100)");
    boxesPerFace = Math.min(Math.max(parseInt(boxesPerFace), 1), 100);
    makeGrid(boxesPerFace);
}

container.addEventListener(("mousedown"), () => {
    isDrawing = true;
});

container.addEventListener(("mouseup"), () => {
    isDrawing = false;
});

container.addEventListener(("mouseover"), (event) => {
    if(isDrawing && event.target.classList.contains("grid-item")) {
        event.target.style.backgroundColor = randomColor();   
        event.target.style.blur();
    }
});

makeGrid(16);
setGrid.addEventListener("click", gridSet);

