package practice;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubdomainVisitCount {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SubdomainVisitCount s = new SubdomainVisitCount();
		String[] cpdomains = { "900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org" };
		System.out.println(s.visitCount(cpdomains));
	}

	private List<String> visitCount(String[] domains) {
		Map<String, Integer> mapdomains = new HashMap<>();
		for (String d : domains) {
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
