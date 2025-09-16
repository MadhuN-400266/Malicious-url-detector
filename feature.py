# feature.py
import re
import socket
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime

class FeatureExtraction:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.whois_response = ""
        try:
            self.whois_response = whois.whois(self.domain)
        except:
            pass

    # 1. Having IP Address
    def having_ip_address(self):
        try:
            socket.inet_aton(self.domain)
            return 1
        except:
            return 0

    # 2. URL Length
    def url_length(self):
        return 1 if len(self.url) < 54 else -1

    # 3. Shortening Service
    def shortening_service(self):
        return -1 if re.search("bit\.ly|tinyurl\.com|goo\.gl", self.url) else 1

    # 4. Having @ symbol
    def having_at_symbol(self):
        return -1 if "@" in self.url else 1

    # 5. Double slash redirecting
    def double_slash_redirecting(self):
        return -1 if self.url.count("//") > 1 else 1

    # 6. Prefix-Suffix in domain
    def prefix_suffix(self):
        return -1 if "-" in self.domain else 1

    # 7. Having Sub Domain
    def having_sub_domain(self):
        return -1 if self.domain.count('.') > 2 else 1

    # 8. SSL final state
    def ssl_final_state(self):
        if self.url.startswith("https"):
            return 1
        else:
            return -1

    # 9. Domain Registration Length
    def domain_registration_length(self):
        try:
            exp_date = self.whois_response.expiration_date
            if isinstance(exp_date, list):
                exp_date = exp_date[0]
            if (exp_date - datetime.now()).days >= 365:
                return 1
            else:
                return -1
        except:
            return -1

    # 10. Favicon
    def favicon(self):
        return 1  # Placeholder

    # 11. HTTPS in URL’s domain part
    def https_token(self):
        return -1 if "https" in self.domain else 1

    # 12. Request URL
    def request_url(self):
        return 1  # Placeholder

    # 13. URL of Anchor
    def url_of_anchor(self):
        return 1  # Placeholder

    # 14. Links in <Meta>, <Script> and <Link> tags
    def links_in_tags(self):
        return 1  # Placeholder

    # 15. SFH (Server Form Handler)
    def sfh(self):
        return 1  # Placeholder

    # 16. Submitting to Email
    def submitting_to_email(self):
        return -1 if "mail()" in self.url or "mailto:" in self.url else 1

    # 17. Abnormal URL
    def abnormal_url(self):
        return -1 if self.whois_response == "" else 1

    # 18. Redirect
    def redirect(self):
        try:
            r = requests.get(self.url, timeout=3)
            if len(r.history) > 1:
                return -1
            else:
                return 1
        except:
            return -1

    # 19. Using pop-up window
    def pop_up_window(self):
        return 1  # Placeholder

    # 20. Iframe redirection
    def iframe_redirection(self):
        return 1  # Placeholder

    # 21. Age of Domain
    def age_of_domain(self):
        try:
            create_date = self.whois_response.creation_date
            if isinstance(create_date, list):
                create_date = create_date[0]
            if (datetime.now() - create_date).days >= 180:
                return 1
            else:
                return -1
        except:
            return -1

    # 22. DNS Record
    def dns_record(self):
        return -1 if self.whois_response == "" else 1

    # 23. Website Traffic (Placeholder)
    def web_traffic(self):
        return 1

    # 24. PageRank (Placeholder)
    def page_rank(self):
        return 1

    # 25. Google Index
    def google_index(self):
        return 1

    # 26. Links pointing to page (Placeholder)
    def links_pointing_to_page(self):
        return 1

    # 27. Stats Report (Placeholder)
    def stats_report(self):
        return 1

    # 28. Having HTTPS in URL
    def https_in_url(self):
        return 1 if "https" in self.url else -1

    # 29. Suspicious words
    def suspicious_words(self):
        return -1 if re.search("secure|account|login|update|banking", self.url) else 1

    # 30. Right Click Disabled (Placeholder)
    def right_click_disabled(self):
        return 1

    def getFeaturesList(self):
        features = [
            self.having_ip_address(),
            self.url_length(),
            self.shortening_service(),
            self.having_at_symbol(),
            self.double_slash_redirecting(),
            self.prefix_suffix(),
            self.having_sub_domain(),
            self.ssl_final_state(),
            self.domain_registration_length(),
            self.favicon(),
            self.https_token(),
            self.request_url(),
            self.url_of_anchor(),
            self.links_in_tags(),
            self.sfh(),
            self.submitting_to_email(),
            self.abnormal_url(),
            self.redirect(),
            self.pop_up_window(),
            self.iframe_redirection(),
            self.age_of_domain(),
            self.dns_record(),
            self.web_traffic(),
            self.page_rank(),
            self.google_index(),
            self.links_pointing_to_page(),
            self.stats_report(),
            self.https_in_url(),
            self.suspicious_words(),
            self.right_click_disabled()
        ]
        return features
