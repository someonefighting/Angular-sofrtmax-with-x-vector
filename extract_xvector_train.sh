#!/bin/bash
rm -rf feat
copy-vector ark:exp/xvectors_sre_combined/xvector.1.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.2.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.3.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.4.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.5.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.6.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.7.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.8.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.9.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.10.ark ark,t:- | head -10 >> feat
copy-vector ark:exp/xvectors_sre_combined/xvector.11.ark ark,t:- | head -10 >> feat
awk -F"[][]" '{print $2}' feat > tmp
sed 's/ //' tmp > feat

