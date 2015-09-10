{
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
	"./src"
      ],
      "link_settings": {
          "libraries": [
              "-L ../lib/<!(node -e \"console.log(require('os').platform() == 'linux' ? 'linux' : 'osx')\")",
              "-lpcap"
          ]
      }
    }
  ]
}
