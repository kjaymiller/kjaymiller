<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script type="text/javascript">
function search(){
  const phrase = document.querySelector('.menu-search').value

  if (phrase.length < 3) {
    hideSearchResultList();
    return null
  }

  else {
    showSearchResultList();
  }

axios.post('https://66893193d66446148486c5cf825496bb.ent-search.us-east-1.aws.cloud.es.io/api/as/v1/engines/kjaymiller/search',
           {"query": "Form Group"},
            {"headers":{"Authorization": "Bearer search-qzy24w1dj5extn1mg8skw92t"}}).then((response) => {console.log(response.data.results[0])})
}


    document.querySelector('.search-results').innerHTML = '';

    for (let result of results.slice(0,5)){
      addSearchResult(result);
    }
  })
  .catch(function (err) {
    console.log(err);
  });
};

function showSearchResultList() {
  document.querySelector('.search-results').classList.add('is-visible');
};

function hideSearchResultList() {
  if (document.querySelector('.search-results').innerHTML) {
      return null
  }

  document.querySelector('.search-results').classList.remove('is-visible');
  document.querySelector('.search-results').classList.add('is-hidden');
};

function addSearchResult(result){
      var div = document.createElement('div');
      div.className = 'navbar-item';

      var a = document.createElement('a');
      a.href = result.item.url;

      if (result.item.title) {
        var linkText = document.createTextNode(result.item.title)
    }

      else {
        var linkText = document.createTextNode(result.item._content.substring(0, 15) + '...')
    }

      a.appendChild(linkText)
      div.appendChild(a)

      document.querySelector('.search-results').appendChild(div)

}

document.querySelector('.menu-search').addEventListener('input', search)
document.querySelector('.menu-search').addEventListener('focusout', hideSearchResultList)
</script>
