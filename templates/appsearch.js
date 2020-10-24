<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script type="text/javascript">

async function post_request(phrase) {
  let response = await fetch('https://66893193d66446148486c5cf825496bb.ent-search.us-east-1.aws.cloud.es.io/api/as/v1/engines/kjaymiller/search',{
      method: "POST",
      body: JSON.stringify({
          "query": phrase,
          "page": {
              "size": 5}
      }),
      headers: {
          "Authorization": "Bearer search-qzy24w1dj5extn1mg8skw92t",
          "content-type": "application/json"
          }
        })
  let search_results = await response.json()
  return search_results
    };

function search() {
  const phrase = document.querySelector('.menu-search').value

  if (phrase.length < 3) {
    hideSearchResultList();
    return null
  }

  else {
    showSearchResultList();
  }

   post_request(phrase).then((results) => {

  for (let result of results){
          addSearchResult(result);
        }
   })

    document.querySelector('.search-results').innerHTML = '';
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
      a.href = result.slug;

      if (result.title) {
        var linkText = document.createTextNode(result.title.raw)
    }

      else {
        var linkText = document.createTextNode("Microblog Post...")
    }

      a.appendChild(linkText)
      div.appendChild(a)

      document.querySelector('.search-results').appendChild(div)

}

document.querySelector('.menu-search').addEventListener('input', search)
document.querySelector('.menu-search').addEventListener('focusout', hideSearchResultList)
</script>
