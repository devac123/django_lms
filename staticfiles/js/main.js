

let urlParams = new URLSearchParams(window.location.search);
let pageCount = urlParams.get('page_count');
if(pageCount){
    jQuery('#p_count').val(pageCount);
}
else{
    jQuery('#p_count').val(10);
}





jQuery('#p_count').on('change', function() {
    
    let current_page = window.location.pathname;
    let urlParams = new URLSearchParams(window.location.search);
    
    // Update or set the 'page_count' query parameter
    urlParams.set('page_count', jQuery(this).val());

    // Redirect to the updated URL
    window.location.href = current_page + '?' + urlParams.toString();
});