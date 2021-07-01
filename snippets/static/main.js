let copyButton = document.querySelector('.btn');
let clipboard = new ClipboardJS('.btn');

      clipboard.on('success', function (e) {
        console.log(e);
      });

      clipboard.on('error', function (e) {
        console.log(e);
      });

      copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
        console.log('click')
        window.location.replace(http://127.0.0.1:8000/snippets/copy)