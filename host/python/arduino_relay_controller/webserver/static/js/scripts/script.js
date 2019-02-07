// $(function() {
//     $('#messageForm').bind('submit', function() {
//         Sijax.request('save_message', [$('#message').attr('value')]);
        
//         //Prevent the form from being submitted
//         return false;
//     });
    
//     $('#message').focus();
    
//     $('#btnClear').bind('click', function() {
//         Sijax.request('clear_messages');
        
//         return false;
//     });
// });
function setOdorValveOn() {
    Sijax.request('setOdorValveOn');
}
function setOdorValvesOff() {
    Sijax.request('setOdorValvesOff');
}
