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
};

function search(phrase){
  fetch('/search.json')
  .then(function (response){
    response.json()})
  .then(function (data) {
      let fuse = new Fuse(data, options)
      return fuse.search(phrase)
  })
  .catch(function (err) {
    console.log(err);
  });
};

</script>

