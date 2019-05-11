#!/bin/bash
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.1.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.2.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.3.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.4.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.5.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.6.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.7.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.8.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.9.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.10.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre16_eval_enroll/xvector.11.ark ark,t:- | head -10 >> feat
awk -F"[][]" '{print $2}' feat > tmp
sed 's/ //' tmp > feat

