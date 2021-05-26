$("#apply").click(function (e) {
    var $this = $(this);
    if ($this.hasClass('clicked')){
        $this.removeClass('clicked'); 
        document.getElementById('message').innerHTML = "You have already applied for this job!";
        //here is your code for double click
    }else{
         $this.addClass('clicked');
         setTimeout(function() { 
             if ($this.hasClass('clicked')){
                 $this.removeClass('clicked'); 
                 document.getElementById('message').innerHTML = "You have applied for this job!"
                 //your code for single click               
             }
         }, 500);          
    }
});