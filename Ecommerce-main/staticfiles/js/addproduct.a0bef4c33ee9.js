function show_other_category(){
    var selectBox = document.getElementById("Category");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    if (selectedValue == "Other"){
        console.log(selectedValue);
        document.getElementById("other_categ_div").style.display = "block";
    }
    else
    {
        console.log(selectedValue)
        document.getElementById("other_categ_div").style.display = "none";
    }
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