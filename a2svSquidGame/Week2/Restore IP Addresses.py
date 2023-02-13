class Solution:
    def restoreIpAddresses(self, s):
        results = []  # this list will hold the valid IP addresses
        self.findAddresses(s, 0, "", results)
        return results

    def findAddresses(self, s, index, currentAddress, results):
        if index == 4:  # if we have 4 sections in the IP address
            if not s:  # and there is no more characters left in the input string
                results.append(currentAddress[:-1])  # add the current address to the results, minus the last dot
            return

        for i in range(1, 4):  # for each possible length of the next section in the IP address
            if i <= len(s):  # if the length is within the bounds of the input string
                # check if the next section is either a single zero or a number between 1 and 255
                if s[:i] == '0' or (s[0] != '0' and int(s[:i]) < 256):
                    self.findAddresses(s[i:], index + 1, currentAddress + s[:i] + ".", results)
