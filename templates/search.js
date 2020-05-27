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
    for (let result of results){
      if (result.item.title) {
        console.log([result.item.title, result.item.url])
    }
      else {
        console.log([result.item._content.substring(0, 15) + '...', result.item.url])
    }
  }
  })
  .catch(function (err) {
    console.log(err);
  });
};

function showSearchResultList() {
  document.querySelector('.search-results').classList.add('is-visible')
};

function hideSearchResultList() {
  document.querySelector('.search-results').classList.remove('is-visible')
};

document.querySelector('.menu-search').
  addEventListener('input', search).
  addEventListener('blur', hideSearchResultList)
</script>

