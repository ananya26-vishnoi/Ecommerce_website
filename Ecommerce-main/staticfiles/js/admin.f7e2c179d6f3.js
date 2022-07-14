function close_modal(){
    document.getElementById('delete_modal').style.display='none';
    document.getElementById('edit_modal').style.display='none';
    document.getElementById("view_modal").style.display='none';
    document.getElementById("add_team_modal").style.display='none';
    document.getElementById('darken').style.overflow="auto";
    document.getElementById('darken').style.opacity="1";
}
function open_modal(name,id){
    document.getElementById('delete_modal').style.display='block';
    document.getElementById('productdeletemodal').innerHTML=name;
    document.getElementById('productdeleteid').innerHTML=id;
    document.getElementById('darken').style.overflow="hidden";
    document.getElementById('darken').style.opacity="0.4";
}

function edit_open_modal(){
    document.getElementById('edit_modal').style.display='block';
    document.getElementById('darken').style.overflow="hidden";
    document.getElementById('darken').style.opacity="0.4";
}
function view_open_modal(){
    document.getElementById("view_modal").style.display='block';
    document.getElementById('darken').style.overflow="hidden";
    document.getElementById('darken').style.opacity="0.4";

}
function open_add_team_modal(){
    document.getElementById("add_team_modal").style.display='block';
    document.getElementById('darken').style.overflow="hidden";
    document.getElementById('darken').style.opacity="0.4";
}

function openNav() {
    document.getElementById("sidebar").style.width = "20%";
    document.getElementById("sidebar").style.backgroundColor = "white";
    document.getElementById("side-opener").style.display = "none";
    }
  
  /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
  function closeNav() {
    document.getElementById("sidebar").style.width = "0px";
    document.getElementById("sidebar").style.backgroundColor = "white";
    document.getElementById("side-opener").style.display = "block";
    
  }
