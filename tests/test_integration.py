from src.packet_analysis.analyze import analyze_pcap

def test_analyze_pcap():
    result = analyze_pcap("example.pcap")
    assert result == "Analyzing example.pcap"