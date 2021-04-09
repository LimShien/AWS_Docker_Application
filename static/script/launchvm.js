//create a split view of the window / launching virtual machine?
$("#launchVM").click(function(){
   $("body").load("/lab1");
    $("#split_one").addClass("left");
    $("#split_two").show();
    $("#splitDiv").show();
    $("#launchVM").hide();
    
    $('#splitDiv').jSplitter({
    'leftdiv': 'split_one',
    'rightdiv': 'split_two',
    'flex': true
    });
  });

//return to original state
 $("#terminateVM").click(function(){
  $("body").load("/lab1");
    $("#split_two").hide();
    $("#splitDiv").hide();
    $("#split_one").removeClass("left");
    $("#launchVM").show();

  })