$(document).ready(function(){
    const CARD_PASS_LEN = 4;
    var inputValue = ''

    function formatCardPassword(){
        subs = "X".repeat(inputValue.length);
        $("#card-pass-input").val(subs);
    };

    $(".btn-ctrl").click(function(){
        //console.log('aaa')
        if ($(this).val() != 'C' && $(this).val() != 'Enter' && inputValue.length < CARD_PASS_LEN) {
            inputValue += $(this).val();
            //console.log(inputValue)
            $("#card-pass").val(inputValue);
            //console.log($("#card-pass").val())
        }
        if ($(this).val() == 'C') {
            inputValue = ''
        }
        //https://github.com/blueimp/JavaScript-MD5
        $("#card-pass").val(md5(inputValue));
        formatCardPassword();
    });
});