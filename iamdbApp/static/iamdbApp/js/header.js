$(document).ready(function(){
    $('#searchBox').keyup(function(){
        //go only for characters not just any key should be searched like backspace,esc,..
        $.ajax({
            url:srchUrl,
            data:{
                'srch_txt':$('#searchBox').val(),
            },
            dataType:'json',
            success:function(data){
                $('#movieListSrch').html("");
                for(let i=0;i<data['movie_details_list'].length;i++){
                    $('#movieListSrch').append("<tr> <td style='text-align:center'><img src='"+data['movie_details_list'][i]['image']+"' height='80px' width='80px'></td> <td><strong>"+data['movie_details_list'][i]['title']+"</strong><br><strong>"+data['movie_details_list'][i]['year']+"</strong></td><td class='icons'><i class='wishIcn fas fa-heart' style='font-size:30px'></i><br><i class='watchedIcn fas fa-check' style='font-size:30px'></i><span class='imdbId' hidden>"+data['movie_details_list'][i]['imdb_id']+"</span></td> </tr>");
                }
//                for(var i=0;i<data['ctObjs'].length;i++){
//                        $('#ctDD').append("<option value='"+data['ctObjs'][i]['id']+"' >"+data['ctObjs'][i]['cityname']+"</option>");
//                }
//                alert();
            },
        });
    });

    $('#movieListSrch').on('click','.watchedIcn',function(){
        $.ajax({
            url:add2watchUrl,
            data:{
                'imdbId':$(this).siblings('.imdbId').html(),
            },
            dataType:'json',
            success:function(data){
                if(data.rslt==1){
                   alert('s');
                }
                else{
                    alert('Error adding to watchlist');
                }
            },
        });

    });
    $('#movieListSrch').on('click','.wishIcn',function(){
        $.ajax({
            url:add2wishUrl,
            data:{
                'imdbId':$(this).siblings('.imdbId').html(),
            },
            dataType:'json',
            success:function(data){
                if(data.rslt==1){
                    alert('s');
                }
                else{
                    alert('Error adding to wishlist');
                }
            },
        });
    });
});