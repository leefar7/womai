// $(function () {
//     $('img').each(function () {
//         var imgPath = $(this).attr('src').replace('img/indeximg','index/img')
//         imgPath = "{% static '"+ imgPath +"' %}"
//         $(this).attr('src',imgPath)
//     })
//     console.log($('body').html())
// })


// $(function () {
//
//     $('img').each(function () {
//
//         var img_path=$(this).attr('src')
//
//         // "{% static 'js/jquery-1.12.3.js' %}"
//         img_new_path="{% static '"+img_path+"' %}"
//         $(this).attr('src',img_new_path)
//     })
//     console.log($('body').html())
// })


// <b style="background: url({% static 'img/indeximg/list01.png' %});">
// $(function () {
//
//     $('i').each(function () {
//
//         var i_path=$(this).attr('style')
//
//         // "{% static 'js/jquery-1.12.3.js' %}"
//         i_new_path="background: url({% static '"+i_path+"' %})"
//         $(this).attr('style',i_new_path)
//     })
//     console.log($('body').html())
// })
// $(function () {
//
//     $('em').each(function () {
//
//         var i_path=$(this).attr('style')
//
//         // "{% static 'js/jquery-1.12.3.js' %}"
//         new_path="background: url({% static '"+i_path+"' %})"
//         $(this).attr('style',new_path)
//     })
//     console.log($('body').html())
// })