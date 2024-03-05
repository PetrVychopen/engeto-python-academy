from bs4 import BeautifulSoup

def extract_center_links(html_content):
  """
  Extracts href attributes from links with class "center" nested within td tags.

  Args:
      html_content: String containing the HTML content.

  Returns:
      A list of strings representing the href attributes of the extracted links.
  """
  soup = BeautifulSoup(html_content, "html.parser")
  links = [td.find("a")["href"] for td \
           in soup.find_all("td", class_="center") if td.find("a")]
  return links