/* 
<!-- Desenvolvido por Leonardo Mantovani -->
<!-- GitHub: https://github.com/LeonardoHMS -->
<!-- Linkedin: https://www.linkedin.com/in/leonardohms/ -->
*/

$(function () {


    //HEADER
    $(window).scroll(function () {
          if($(this).scrollTop() > 200)
          {
              if (!$('.main_header').hasClass('fixed'))
              {
                  $('.main_header').stop().addClass('fixed').css('top', '-100px').animate(
                      {
                          'top': '0px'
                      }, 500);
              }
          }
          else
          {
              $('.main_header').removeClass('fixed');
          }
    });


    //Código jQuery para adicionar o efeito zebra na tabela.
    $(document).ready(function() {

       $('#tabela tbody tr:odd').addClass('impar');
     //$('#tabela tbody tr:even').addClass('par');
    
    });


});


const INPUT_SEARCH = document.getElementById('input-search');
const PDF_TABLE = document.getElementById('pdf-table');
const THEAD_DISPLAY = document.getElementById('thead-display');
const INTRO_DISPLAY = document.getElementById('message-intro-id');
const NOT_FOUND_DISPLAY = document.getElementById('message-not-found-id');
const SCREEN_LOAD = document.getElementById('loading-page');

SCREEN_LOAD.style.display = 'none';
NOT_FOUND_DISPLAY.style.display = 'none';

document.addEventListener('keypress', function(e){
    if(e.which == 13){
       search();
    }
 }, false);

function search(expression) {
    expression = INPUT_SEARCH.value.toLowerCase().trim();

    let lines = PDF_TABLE.getElementsByTagName('tr');
    var found_files = 0;

    for (let position in lines) {
        if (true === isNaN(position)) {
            continue;
        }
        let lineContent = lines[position].innerHTML.toLowerCase();

        if (true === lineContent.includes(expression)) {
            lines[position].style.display = '';
            lines[position].classList.add('visible');
            found_files = found_files + 1;
        } else {
            lines[position].style.display = 'none';
            lines[position].classList.remove('visible');
        }
    }

    if (found_files === 0) {
        NOT_FOUND_DISPLAY.style.display = '';
        THEAD_DISPLAY.style.display = 'none';
    } else {
        NOT_FOUND_DISPLAY.style.display = 'none';
        THEAD_DISPLAY.style.display = '';
    }

    INTRO_DISPLAY.style.display = 'none';
};

function restaure() {
    let lines = PDF_TABLE.getElementsByTagName('tr');
    THEAD_DISPLAY.style.display = 'none';
    INTRO_DISPLAY.style.display = '';
    NOT_FOUND_DISPLAY.style.display = 'none';
    for (let position in lines) {
        lines[position].style.display = 'none';
        lines[position].classList.remove('visible');
    }
};


const closeModalButton = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");
const embedScr = document.querySelector('embed');

const toggleModal = () => {
    [modal, fade].forEach((el) => el.classList.toggle("hide"));
};

[closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
});


function OpenPdf(srcPdf) {
    embedScr.src = srcPdf;
    toggleModal();
};

function CopyText(value){
    navigator.clipboard.writeText(value);
}

const LINES_TABLE = document.getElementsByTagName('tr');
for (let position in LINES_TABLE) {
    LINES_TABLE[position].style.display = 'none';
};