console.log('Hola javascript 2.0')

var cover = document.getElementById('cover')
var learn_more = document.getElementById('btn_learn')
var get_next = document.getElementById('btn_next')
var self_doubt = document.getElementById('self_doubt')


self_doubt.addEventListener("click", affirmation);
learn_more.addEventListener("click", follow_url);
get_next.addEventListener("click", get_new);


function get_new(){
    fetch("/til")
    .then(response => response.json())
    .then(data => {
    cover.innerHTML=`
              <h1 class="cover-heading">Today I learned.</h1>
              <p class="lead" id="quote">${data.title}</p>
              <p class="lead">
                <a href="#" class="betn btn-lg btn-success" id ="btn_next">Get Another One</a>
                <a href="${data.url}" class="btn btn-lg btn-info" id="btn_learn" target="_blank">Learn more</a>
              </p>
              <p>This is for fun too</p>
    `;
    var get_next = document.getElementById('btn_next')
    get_next.addEventListener("click", get_new);
    })
}

function follow_url(){
    window.open(get_next.href,"new");
}

function affirmation(){
    self_doubt.classList.add('active');
    var home_link = document.getElementById('home_link')
    home_link.classList.remove('active');
    fetch("/affirmations")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        cover.innerHTML=`
        <h1 class="cover-heading">${data.affirmation}</h1>
        `
    })

}

get_new()


