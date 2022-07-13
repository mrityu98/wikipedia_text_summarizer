function f()
{
    if(url!="" && fr!="")
    {
    var url=document.getElementById("search1").value;
    var fr=document.getElementById("search2").value;
    document.getElementById("loader").style.display='block'; 
}}
function is_empty()
{     
var url= document.getElementById("search1").value;
var fr=document.getElementById("search2").value;
if(url!="" && fr!="")
{
const arr=url.split("/")
if(arr.length == 5 || arr.length == 6)
{
    if(arr[0]=="https:" && arr[1]=="" && arr[2]=="en.wikipedia.org" && arr[3]=="wiki" && arr[4].length>0)
{
document.getElementById("but").removeAttribute("disabled");
}
}
}
}


