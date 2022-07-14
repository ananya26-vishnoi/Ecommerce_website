function showothercategory(){
        document.getElementById("other_categ_div").style.display = document.getElementById("other_categ_show").checked ? "block" : "none";
}
var i=1
function addfeature(){
    i++
    var div = "<div class = 'user-box' id='feature-"+i+"'><input name='feature-"+i+"-input' class='fullwidth features_user_box' id='feature-"+i+"-input' type='text' required><label>Feature -"+ i+"</label></div> "
    $("#features").append(div);
}
function removefeature(){
    if(i>1){
        $("#feature-"+i).remove();
        i--;
    }
}