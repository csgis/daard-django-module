
import os

layername = os.getenv('DAARD_LAYERNAME', "daard_database")

update_sql = f"UPDATE public.{layername} " \
             "SET the_geom=ST_MakePoint((%s),(%s))," \
             "is_approved=%s," \
             "\"owner\"=%s," \
             "uuid=%s," \
             "adults=%s," \
             "subadults=%s," \
             "disease=%s," \
             "age_class=%s," \
             "age=%s," \
             "age_freetext=%s," \
             "sex=%s," \
             "bone_relations=%s," \
             "reference_images=%s," \
             "origin=%s," \
             "site=%s," \
             "gazid=%s," \
             "gaz_link=%s," \
             "archaeological_tombid=%s," \
             "archaeological_individualid=%s," \
             "archaeological_funery_context=%s," \
             "archaeological_burial_type=%s," \
             "storage_place=%s," \
             "storage_place_freetext=%s," \
             "chronology=%s," \
             "chronology_freetext=%s," \
             "dating_method=%s," \
             "dna_analyses=%s," \
             "dna_analyses_link=%s," \
             "published=%s," \
             "doi=%s," \
             "c_bones=%s," \
             "c_no_o_bones=%s," \
             "c_b_t_bc_rel=%s," \
             "c_technic=%s," \
             "svgid=%s," \
             "\"references\"=%s" \
             " WHERE \"uuid\"=%s;"

insert_sql = f"INSERT INTO public.{layername} " \
             f"(the_geom, " \
             f"is_approved, " \
             f"\"owner\", " \
             f"uuid, " \
             f"adults, " \
             f"subadults, " \
             f"disease, " \
             f"age_class, " \
             f"age, " \
             f"age_freetext, " \
             f"sex, " \
             f"bone_relations, " \
             f"reference_images, " \
             f"origin, " \
             f"site, " \
             f"gazid, " \
             f"gaz_link, " \
             f"archaeological_tombid, " \
             f"archaeological_individualid," \
             f"archaeological_funery_context, " \
             f"archaeological_burial_type, " \
             f"storage_place, " \
             f"storage_place_freetext, " \
             f"chronology, " \
             f"chronology_freetext, " \
             f"dating_method, " \
             f"dna_analyses, " \
             f"dna_analyses_link, " \
             f"published, " \
             f"doi, " \
             f"c_bones, " \
             f"c_no_o_bones, " \
             f"c_b_t_bc_rel, " \
             f"c_technic," \
             f"svgid, " \
             f"\"references\")" \
             f"VALUES" \
             f"(ST_MakePoint((%s),(%s)), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s), " \
             f"(%s));"

sql_delete_str = f"DELETE FROM public.{layername} " \
                 f"WHERE uuid=%s;"
