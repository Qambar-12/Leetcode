class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = []
        for email in emails:
            parts = email.split('@')
            local = parts[0]
            domain = parts[1]
            if '+' in local:
                index = local.find('+')
                local = local[:index]
            if '.' in local:
                local = local.replace('.','')
            email = local +'@'+domain
            if email not in unique:
                unique.append(email)
        return len(unique)            
