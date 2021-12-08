class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> mapdomains = new HashMap<>();
		for (String d : cpdomains) {
			String[] parts = d.split(" ");
			int visits = Integer.parseInt(parts[0]);
			String fullDomain = parts[1];
			String[] domainParts = fullDomain.split("\\.");
			String suffix = "";
			for (int i = domainParts.length - 1; i >= 0; i--) {
				String domainPart = domainParts[i];
				if (i == domainParts.length - 1) {
					suffix = domainPart;
				} else {
					suffix = domainPart + "." + suffix;
				}
				mapdomains.put(suffix, mapdomains.getOrDefault(suffix, 0) + visits);
			}
		}
		List<String> res = new ArrayList<>();
		for (Map.Entry<String, Integer> entry : mapdomains.entrySet()) {
			res.add(entry.getValue() + " " + entry.getKey());
		}
		return res;
    }
}