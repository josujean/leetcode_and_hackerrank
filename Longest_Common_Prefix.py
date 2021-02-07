class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if len(strs) > 0:
            for letter in strs[0]:
                if all([s.startswith(common_prefix + letter) for s in strs]):
                    common_prefix += letter

        return common_prefix
        
