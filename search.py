from elastic_enterprise_search import EnterpriseSearch
import hashlib

client = AppSearch(
        os.environ['APP_SEARCH_ENDPOINT'],
        http_auth=['APP_SEARCH_API_KEY'],
        )


def id_hash(page: Page, *id_fields) -> str:
    """Generate a Hash from the provided fields"""
    raw_msg = "".join([getattr(page, x, "") for x in id_fields]).encode("utf-8")
    return hashlib.sha1(raw_msg).hexdigest()


def build_index(pages: typing.Sequence[Page], id_field: str="_id", **search_params):
     """Build a page dict for the keys requested. There is a
     question if this should be replaced with a __dict__ overwrite on page."""

     for page in pages:
         page_dict = page.__dict__()

                 if key == "slug":
                     page_dict['slug'] = f"{search_params['site_url']}/{field_value}"

                 elif key_params["type"] == "date":
                     page_dict[key] = field_value.to_rfc3339_string()

                 else:
                     page_dict[key] = field_value

         page_dict[id_field] = _id_hash(page, *search_params["id_fields"])

         yield page_dict


def document(Page):
    if page.noindex():
        return None

    else:
        doc = {
                'title': page.title
                }
        return doc


