
window.onload = () => {

  $("#ImageStream").hide();
  $("#sendbutton").click(() => {
  console.log("Analyse Button Clicked")
    imagebox = $("#imagebox");
    link = $("#link");
    input = $("#imageinput")[0];
    console.log(Inputflag)
    $("#ImageStream").show();
     $("#sendbutton").hide();
     $("#Stop").show();
    if (Inputflag=="FileInput"){
        if (input.files && input.files[0]) {
          let formData = new FormData();
          formData.append("Video", input.files[0]);
          formData.append("InputType", "Inputfile");
            $("#choosefileDiv").hide();
          $.ajax({
            url: "/detect", // fix this to your liking
            type: "POST",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            error: function (data) {
              console.log("upload error", data);
              console.log(data.getAllResponseHeaders());
            },
            success: function (data) {
              console.log(data);

              // bytestring = data["status"];
              // image = bytestring.split("'")[1];
//              $("#link").css("visibility", "visible");
//              $("#download").attr("href", "static/" + data);
              console.log(data);
            },
          });
        }
    }

    if (Inputflag=="URLInput") {
        VIDEO_URL = $('#VIDEO_URL')
        TextboxValue = VIDEO_URL.val()

        $("#URLTEXTDIV").hide();
        if (TextboxValue.startsWith("http")) {
          let formData = new FormData();
          formData.append("Video", TextboxValue);
          formData.append("InputType", "URL");
          $.ajax({
            url: "/detect", // fix this to your liking
            type: "POST",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            error: function (data) {
              console.log("upload error", data);
              console.log(data.getAllResponseHeaders());
            },
            success: function (data) {
              console.log(data);
              // bytestring = data["status"];
              // image = bytestring.split("'")[1];
              $("#link").css("visibility", "visible");
              $("#download").attr("href", "static/" + data);
              console.log(data);
            },
          });
        }


    }
  });

  $("#Stop").click(() => {
            let formData1 = new FormData();
            formData1.append("Flag", "KILL");
            window.location.reload();
            $.ajax({
            url: "/Stopprocess", // fix this to your liking
            type: "POST",
            data: formData1,
            cache: false,
            processData: false,
            contentType: false,
            error: function (data) {
              console.log("upload error", data);
              console.log(data.getAllResponseHeaders());
            },
            success: function (data) {
              console.log(data);
              // bytestring = data["status"];
              // image = bytestring.split("'")[1];



            },
          });



  });

};
function displayURLTextBox(){
 URLDIV = $('#URLTEXTDIV')
 DisplayDIV = $('#inputDIV')
URLDIV.show();
DisplayDIV.hide();
Inputflag = "URLInput"

}
function displayInputBOX(){
 choosefileDiv = $('#choosefileDiv')
 DisplayDIV = $('#inputDIV')
Inputflag = "FileInput"
choosefileDiv.show();
DisplayDIV.hide();

}


//$('#rateToPost').on("change", function () {
//  alert($(this).val());
//});

function displayAnalyseButton(){
VIDEO_URL = $('#VIDEO_URL')
console.log("Button CLicked")
TextboxValue = VIDEO_URL.val()
if(TextboxValue.startsWith("http"))
{

$('#sendbutton').show()

}
else
{
$('#sendbutton').hide()
}

}
function readUrl(input) {
  imagebox = $("#imagebox");
  console.log(imagebox);
  console.log("evoked readUrl");
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      console.log(e.target);
      $('#sendbutton').show()

//      imagebox.attr("src", e.target.result);
      //   imagebox.height(500);
      //   imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
  else{
  $('#sendbutton').hide()
  }
}

function changeValue(url){
$('#VIDEO_URL').val(url);
$('#sendbutton').show()
}

