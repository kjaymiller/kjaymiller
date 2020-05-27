<script src="https://cdn.jsdelivr.net/npm/fuse.js@6.0.0"></script>
<script type="text/javascript">

const options = {
  // isCaseSensitive: false,
  // includeScore: false,
  // shouldSort: true,
  // includeMatches: false,
  // findAllMatches: false,
  // minMatchCharLength: 1,
  // location: 0,
  // threshold: 0.6,
  // distance: 100,
  // useExtendedSearch: false,
  keys: [
    'title',
    '_content'
  ]
};

function search(){
  const phrase = document.querySelector('.menu-search').value

  if (phrase.length < 3) {
    return null
  }

  else {
    showSearchResultList();
  }

  fetch('/search.json')
  .then(function (response){
    return response.json()})
  .then(function (data) {
      let fuse = new Fuse(data, options);
      results = fuse.search(phrase)

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
  document.querySelector('.search-results').classList.remove('is-visible');
  document.querySelector('.search-results').innerHTML = '';
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

