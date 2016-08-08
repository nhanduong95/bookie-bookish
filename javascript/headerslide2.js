$(function() {
    var currentindex = 1;
    display($('#headercontent li:nth-child(2)'));
                
    $('#headercontent li').click(function(){
        display($(this));
    });
                
    function display(element){
        var $this = element;
        var slidein = false;
        if(currentindex == parseInt($this.index() + 1))
            slidein = true;
                    
        else
            $this
            .parent()
            .find('li:nth-child('+currentindex+') .headerbut')
            .stop(true,true)
            .animate(300,function(){
                $(this).animate({'opacity':'0.6'},700);
            });
                    
        currentindex = parseInt($this.index() + 1);            
        var element = $('.headerbut',$this);      
        element.stop(true,true).animate({'opacity':'1.0'},300);
                    
        var element_details = element.next();
        $('#headerdisplay .title').animate({'left':'-400px'}, 300,function(){
            $('h1',$(this)).html(element_details.find('.headertitle').html());
            $(this).animate({'left':'50px'},400);
        });
                    
        $('#headerdisplay .info').animate({'bottom':'-10px','left':'-550px'},300,'easeOutCirc',function(){
            $('.para',$(this)).html(element_details.find('.headerinfo').html());
            $(this).animate({'bottom':'0px','left':'0px'},300,'easeInCirc');
        })
                    
        $('#headerdisplay').prepend(
            $('<img/>',{style :'opacity:0', className : 'bg'}).load(function(){
                $(this).animate({'opacity':'1'},300);
                $('#headerdisplay img:first')
                    .next()
                    .animate({'opacity':'0'},400,function(){$(this).remove();});
            }).attr('src','images/'+element_details.find('.headerimage').html()).attr('width','1030')
        );
    }
})