const { ipcRenderer } = require('electron')
const ipc = ipcRenderer

minimize.addEventListener('click', () => {
    ipc.send('minimizaapp')
})

closebtn.addEventListener('click', () => {
    ipc.send('closeapp')
})