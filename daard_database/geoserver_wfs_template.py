header = '''<?xml version="1.0" encoding="UTF-8"?>
<wfs:Transaction xmlns:wfs="http://www.opengis.net/wfs" xmlns:geonode="http://www.geonode.org/" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" service="WFS" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/wfs">'''

footer = '''</wfs:Transaction>'''

# Todo: Read schema from OWS-lib
update_body = '''
    <wfs:Update typeName="{layername}">
        <wfs:Property>
          <wfs:Name>is_approved</wfs:Name>
          <wfs:Value>{is_approved}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>owner</wfs:Name>
          <wfs:Value>{owner_id}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>adults</wfs:Name>
          <wfs:Value>{adults}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>subadults</wfs:Name>
          <wfs:Value>{subadults}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>disease</wfs:Name>
          <wfs:Value>{disease_id}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>age_class</wfs:Name>
          <wfs:Value>{age_class}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>age</wfs:Name>
          <wfs:Value>{age}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>age_freetext</wfs:Name>
          <wfs:Value>{age_freetext}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>sex</wfs:Name>
          <wfs:Value>{sex}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>bone_relations</wfs:Name>
          <wfs:Value>{bone_relations}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>reference_images</wfs:Name>
          <wfs:Value>{reference_images}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>origin</wfs:Name>
          <wfs:Value>{origin}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>site</wfs:Name>
          <wfs:Value>{site}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>gazid</wfs:Name>
          <wfs:Value>{gazId}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>gaz_link</wfs:Name>
          <wfs:Value>{gaz_link}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>archaeological_tombid</wfs:Name>
          <wfs:Value>{archaeological_tombid}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>archaeological_individualid</wfs:Name>
          <wfs:Value>{archaeological_individualid}</wfs:Value>
        </wfs:Property>       
        <wfs:Property>
          <wfs:Name>archaeological_funery_context</wfs:Name>
          <wfs:Value>{archaeological_funery_context}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>archaeological_burial_type</wfs:Name>
          <wfs:Value>{archaeological_burial_type}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>storage_place</wfs:Name>
          <wfs:Value>{storage_place}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>storage_place_freetext</wfs:Name>
          <wfs:Value>{storage_place_freetext}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>storage_condition</wfs:Name>
          <wfs:Value>{storage_condition}</wfs:Value>
        </wfs:Property>        
        <wfs:Property>
          <wfs:Name>chronology</wfs:Name>
          <wfs:Value>{chronology}</wfs:Value>
        </wfs:Property>        
         <wfs:Property>
          <wfs:Name>chronology_freetext</wfs:Name>
          <wfs:Value>{chronology_freetext}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>dating_method</wfs:Name>
          <wfs:Value>{dating_method}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>dna_analyses</wfs:Name>
          <wfs:Value>{dna_analyses}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>dna_analyses_link</wfs:Name>
          <wfs:Value>{dna_analyses_link}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>published</wfs:Name>
          <wfs:Value>{published}</wfs:Value>
        </wfs:Property>
         <wfs:Property>
          <wfs:Name>publication_link</wfs:Name>
          <wfs:Value>{publication_link}</wfs:Value>
        </wfs:Property>         
        <wfs:Property>
          <wfs:Name>c_no_o_bones</wfs:Name>
          <wfs:Value>{c_no_o_bones}</wfs:Value>
        </wfs:Property>
        <wfs:Property>
          <wfs:Name>c_bones</wfs:Name>
          <wfs:Value>{c_bones}</wfs:Value>
        </wfs:Property>     
        <wfs:Property>
          <wfs:Name>c_b_t_bc_rel</wfs:Name>
          <wfs:Value>{c_b_t_bc_rel}</wfs:Value>
        </wfs:Property>  
        <wfs:Property>
          <wfs:Name>c_technic</wfs:Name>
          <wfs:Value>{c_technic}</wfs:Value>
        </wfs:Property> 
        <wfs:Property>
            <wfs:Name>the_geom</wfs:Name>
                 <wfs:Value>
                    <gml:Point srsDimension="2" srsName="EPSG:4326">
                       <gml:pos>{position}</gml:pos>
                    </gml:Point>
                 </wfs:Value>
        </wfs:Property>
        <ogc:Filter>
            <ogc:PropertyIsEqualTo>
               <ogc:PropertyName>uuid</ogc:PropertyName>
               <ogc:Literal>{uuid}</ogc:Literal>
            </ogc:PropertyIsEqualTo>
        </ogc:Filter>
    </wfs:Update>
    '''

create_body = '''
    <wfs:Insert><{layername}>
        <geonode:is_approved>{is_approved}</geonode:is_approved>
        <geonode:owner>{owner_id}</geonode:owner>
        <geonode:uuid>{uuid}</geonode:uuid>
        <geonode:adults>{adults}</geonode:adults>
        <geonode:subadults>{subadults}</geonode:subadults>
        <geonode:disease>{disease_id}</geonode:disease>
        <geonode:age_class>{age_class}</geonode:age_class>
        <geonode:age>{age}</geonode:age>
        <geonode:age_freetext>{age_freetext}</geonode:age_freetext>
        <geonode:sex>{sex}</geonode:sex>
        <geonode:bone_relations>{bone_relations}</geonode:bone_relations>
        <geonode:reference_images>{reference_images}</geonode:reference_images>
        <geonode:origin>{origin}</geonode:origin>
        <geonode:site>{site}</geonode:site>
        <geonode:gazid>{gazId}</geonode:gazid>
        <geonode:gaz_link>{gaz_link}</geonode:gaz_link>
        <geonode:archaeological_tombid>{archaeological_tombid}</geonode:archaeological_tombid>
        <geonode:archaeological_individualid>{archaeological_individualid}</geonode:archaeological_individualid>
        <geonode:archaeological_funery_context>{archaeological_funery_context}</geonode:archaeological_funery_context>
        <geonode:archaeological_burial_type>{archaeological_burial_type}</geonode:archaeological_burial_type>
        <geonode:storage_place>{storage_place}</geonode:storage_place>
        <geonode:storage_place_freetext>{storage_place_freetext}</geonode:storage_place_freetext>
        <geonode:storage_condition>{storage_condition}</geonode:storage_condition>
        <geonode:chronology>{chronology}</geonode:chronology>
        <geonode:chronology_freetext>{chronology_freetext}</geonode:chronology_freetext>
        <geonode:chronology_freetext>{chronology_freetext}</geonode:chronology_freetext>
        <geonode:dating_method>{dating_method}</geonode:dating_method>
        <geonode:dna_analyses>{dna_analyses}</geonode:dna_analyses>
        <geonode:dna_analyses_link>{dna_analyses_link}</geonode:dna_analyses_link>
        <geonode:published>{published}</geonode:published>
        <geonode:publication_link>{publication_link}</geonode:publication_link>   
        <geonode:c_no_o_bones>{c_no_o_bones}</geonode:c_no_o_bones>   
        <geonode:c_bones>{c_bones}</geonode:c_bones>           
        <geonode:c_b_t_bc_rel>{c_b_t_bc_rel}</geonode:c_b_t_bc_rel>   
        <geonode:c_technic>{c_technic}</geonode:c_technic>   
        <geonode:the_geom>
            <gml:Point srsDimension="2" srsName="EPSG:4326">
                <gml:pos>{position}</gml:pos>
            </gml:Point>
        </geonode:the_geom>
        </{layername}>
    </wfs:Insert>
        '''


wfs_insert_tpl = header + create_body + footer
wfs_update_tpl = header + update_body + footer


wfs_delete_tpl = header + '''<wfs:Delete typeName="{layerName}">
      <ogc:Filter>
         <ogc:Or>
            <ogc:PropertyIsEqualTo>
               <ogc:PropertyName>geoserver_id</ogc:PropertyName>
               <ogc:Literal>{uuid}</ogc:Literal>
            </ogc:PropertyIsEqualTo>
         </ogc:Or>
      </ogc:Filter>
   </wfs:Delete>
''' + footer