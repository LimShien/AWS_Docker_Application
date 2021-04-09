  

  //launching and terminating machine
  $("#launchMachine").click(function(){
    $(".machineInfo").show();
    $("#launchMachine").hide();
    countdown();

  })

  $("#terminateMachine").click(function(){
    $(".machineInfo").hide();
    $("#launchMachine").show();

  })
  
  //countdown timer
 
    function countdown(){

      var countdown = new Date();
      countdown.setHours( countdown.getHours() + 2 );

      var x = setInterval(function(){ //update countdown every second

      var now = new Date().getTime();//get the current time

      var d = countdown - now;

      //hours, minutes, seconds
      var hours = Math.floor((d % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((d % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((d % (1000 * 60)) / 1000);

      //output 
     document.getElementById("countdowntimer").innerHTML = hours + "h "+ minutes + "m " + seconds + "s ";
      
      //the countdown over, terminate the machine
      if (d < 0) {
        clearInterval(x);
        document.getElementById("countdowntimer").innerHTML = "EXPIRED";
        $(".machineInfo").hide();
        $("#launchMachine").show();
      }
      }, 1000);
    } //end of function countdown()

  $("#addTime").click(function(){
      
  })