# From AutoSQLi


class Target:
    url = ""
    waf_detection_done = False
    is_protected_by_waf = False
    working_tampers = []
    sqlmap_exploitation_done = False
    is_vulnerable = False

    def __init__(self, url):
        """ create a new Target """
        self.url = url

    def setWaf(self, isProtectedByWaf):
        """ specify if the target is protected by a WAF """
        self.is_protected_by_waf = isProtectedByWaf


def urls_to_targets(urls):
    """ convert an url array to a Target array """
    target_list = []
    for url in urls:
        target_list.append(Target(url))

    return target_list