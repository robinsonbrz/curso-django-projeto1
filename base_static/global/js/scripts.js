function my_scope() {
    const forms = document.querySelectorAll('.form-delete');
  
    for (const form of forms) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
  
        const confirmed = confirm('Are you sure?');
  
        if (confirmed) {
          form.submit();
        }
      });
    }

  console.log("carregamento")

    // carregamento de thumbs
    // descontinuado
    /*
    $(".recipe-img-th").each(function() {            
      console.log("####")
      a =$(this).attr("alt").replace("15/","15/th-")

      console.log(a)	
    $(this).attr("src", a)
    $(this).attr("alt", "")
   });
   */




  }
  
  my_scope();