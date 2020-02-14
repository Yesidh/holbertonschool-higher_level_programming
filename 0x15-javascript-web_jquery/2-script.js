/*
avascript script that updates the text color of the HTML tag HEADER
 to red (#FF0000) when the user clicks on the tag DIV#red_header
*/

$('#red_header').click(function () {
  $(this).css('color', '#FF0000');
});
