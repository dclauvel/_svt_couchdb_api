// view for nsx_edge docs
// returns interfaces sub-jsons


function(doc) {
    
    var key ; 
    var normalized_interfaces = [] ;
    
    if (doc.svt_collect_date 
            && doc.svt_client
            && doc.svt_source
            && doc.svt_source_file
            && doc.svt_source_file.indexOf("nsx_edge") != -1
            && doc.interfaces
            && doc.interfaces.interfaces
            && doc.id
        
        ) {
        
        // name the fields
        collect = doc.svt_collect_date ;
        client = doc.svt_client ;
        source = doc.svt_source ;
        id = doc.id ;
        interfaces = doc.interfaces.interfaces ;
        
        // loop the features & find the correct one
        interfaces.forEach(function(iface) {
            var v = {} ;
            if (iface.label) {
                v.svt_unic = iface.label ;
                v.svt_value = iface ;
                normalized_interfaces.push(v) ; 
            }
        }) ;

        // map all vnics   
        key = [collect, client, source, id]  ;
        emit( key,  {"interfaces":normalized_interfaces, 'svt_action':'svt_standard'} );
        
    }
}
