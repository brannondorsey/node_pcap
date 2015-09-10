{
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "link_settings": {
          "libraries": [
              "-rpath ./lib/<!(node -e \"console.log(require('os').hostname() === 'linux' ? 'linux' : 'osx')\")/libpcap.a"
          ]
      }
    }
  ]
}
